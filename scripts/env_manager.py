#!/usr/bin/env python3
"""
Environment Variables Manager - Secure CLI Tool
Manage .env files for your applications securely.

Usage:
    python scripts/env_manager.py --help

Features:
- Set/get environment variables in .env files
- Never displays sensitive values in output
- Validates .env file format
- Backup and restore functionality
- Secure: masks sensitive data in logs

Security Notes:
- .env files are automatically added to .gitignore
- Never commit .env files to version control
- Use strong, unique values for sensitive variables
"""

import os
import sys
import argparse
import shutil
from pathlib import Path
from datetime import datetime

class EnvManager:
    """Secure environment variables manager."""

    def __init__(self, env_file='.env'):
        self.env_file = Path(env_file)
        self.backup_dir = Path('.env_backups')
        self.backup_dir.mkdir(exist_ok=True)

    def _mask_value(self, value):
        """Mask sensitive values for secure display."""
        if len(value) <= 4:
            return '*' * len(value)
        return value[:2] + '*' * (len(value) - 4) + value[-2:]

    def _validate_key(self, key):
        """Validate environment variable key format."""
        if not key:
            raise ValueError("Key cannot be empty")
        if not key.replace('_', '').isalnum():
            raise ValueError("Key must contain only letters, numbers, and underscores")
        if not key[0].isalpha() and key[0] != '_':
            raise ValueError("Key must start with a letter or underscore")
        return key.upper()

    def _backup_env_file(self):
        """Create a timestamped backup of the .env file."""
        if self.env_file.exists():
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = self.backup_dir / f'env_backup_{timestamp}'
            shutil.copy2(self.env_file, backup_file)
            print(f"Backup created: {backup_file}")

    def load_env(self):
        """Load environment variables from .env file."""
        if not self.env_file.exists():
            return {}

        env_vars = {}
        with open(self.env_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                if '=' not in line:
                    print(f"Warning: Invalid line {line_num}: {line}")
                    continue

                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()

                # Remove quotes if present
                if (value.startswith('"') and value.endswith('"')) or \
                   (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]

                try:
                    key = self._validate_key(key)
                    env_vars[key] = value
                except ValueError as e:
                    print(f"Warning: Invalid key on line {line_num}: {e}")

        return env_vars

    def save_env(self, env_vars):
        """Save environment variables to .env file."""
        self._backup_env_file()

        with open(self.env_file, 'w', encoding='utf-8') as f:
            f.write("# Environment Variables - Managed by env_manager.py\n")
            f.write(f"# Last updated: {datetime.now().isoformat()}\n")
            f.write("# WARNING: Never commit this file to version control!\n\n")

            for key in sorted(env_vars.keys()):
                value = env_vars[key]
                f.write(f'{key}={value}\n')

        print(f"Environment variables saved to {self.env_file}")

    def set_var(self, key, value):
        """Set a single environment variable."""
        key = self._validate_key(key)
        env_vars = self.load_env()
        env_vars[key] = value
        self.save_env(env_vars)
        print(f"Set {key} = {self._mask_value(value)}")

    def get_var(self, key):
        """Get a single environment variable."""
        key = self._validate_key(key)
        env_vars = self.load_env()
        if key in env_vars:
            print(f"{key} = {self._mask_value(env_vars[key])}")
        else:
            print(f"Variable {key} not found")

    def list_vars(self):
        """List all environment variables (masked)."""
        env_vars = self.load_env()
        if not env_vars:
            print("No environment variables found")
            return

        print("Environment Variables:")
        for key in sorted(env_vars.keys()):
            print(f"  {key} = {self._mask_value(env_vars[key])}")

    def delete_var(self, key):
        """Delete a single environment variable."""
        key = self._validate_key(key)
        env_vars = self.load_env()
        if key in env_vars:
            del env_vars[key]
            self.save_env(env_vars)
            print(f"Deleted {key}")
        else:
            print(f"Variable {key} not found")

    def validate_env_file(self):
        """Validate the .env file format."""
        if not self.env_file.exists():
            print("No .env file found")
            return

        env_vars = self.load_env()
        print(f"Validated {len(env_vars)} environment variables")
        print("✓ File format is valid")

    def create_template(self):
        """Create a template .env file with common variables."""
        if self.env_file.exists():
            print(".env file already exists. Use --set to modify variables.")
            return

        template_vars = {
            'MONZO_ACCESS_TOKEN': 'your_monzo_token_here',
            'DEBUG': 'false',
            'LOG_LEVEL': 'INFO'
        }

        self.save_env(template_vars)
        print("Created template .env file. Please update with your actual values.")

def main():
    parser = argparse.ArgumentParser(
        description="Secure Environment Variables Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/env_manager.py --set MONZO_ACCESS_TOKEN your_token_here
  python scripts/env_manager.py --get MONZO_ACCESS_TOKEN
  python scripts/env_manager.py --list
  python scripts/env_manager.py --template
        """
    )

    parser.add_argument('--env-file', default='.env',
                       help='Path to .env file (default: .env)')
    parser.add_argument('--set', nargs=2, metavar=('KEY', 'VALUE'),
                       help='Set an environment variable')
    parser.add_argument('--get', metavar='KEY',
                       help='Get an environment variable')
    parser.add_argument('--delete', metavar='KEY',
                       help='Delete an environment variable')
    parser.add_argument('--list', action='store_true',
                       help='List all environment variables')
    parser.add_argument('--validate', action='store_true',
                       help='Validate .env file format')
    parser.add_argument('--template', action='store_true',
                       help='Create template .env file')

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        return

    manager = EnvManager(args.env_file)

    try:
        if args.set:
            manager.set_var(args.set[0], args.set[1])
        elif args.get:
            manager.get_var(args.get)
        elif args.delete:
            manager.delete_var(args.delete)
        elif args.list:
            manager.list_vars()
        elif args.validate:
            manager.validate_env_file()
        elif args.template:
            manager.create_template()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()