# Changelog

All notable changes to this project will be documented in this file.
The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Latest

- Added timestamp fields to track when records are added.

## 0.2.0 (2025-07-15)

- Changed the models to used the natural keys in the eBird data: Country codes (US),
  Checklist identifiers (S259543824), etc.

## 0.1.1 (2025-07-14)

- Removed composite name (name/original) from the Location and Observer changelists
  in the Django Admin.

## 0.1.0 (2025-07-10)

Initial release from code developed for https://www.ebirders.pt/. Despite the
version number, the code is in production, and is very stable, and reliable.
