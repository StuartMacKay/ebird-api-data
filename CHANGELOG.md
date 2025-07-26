# Changelog

All notable changes to this project will be documented in this file.
The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Latest

## 0.3.5 (2025-07-26)

- Change Checklist.Protocol from a TextChoice to a regular python class so the 
  list of protocols can be updated.

## 0.3.4 (2025-07-25)

- Change Checklist.get_protocol() to lookup name not code.

## 0.3.3 (2025-07-25)

- Added Checklist.get_protocol() to return the name for the protocol_code attribute.

## 0.3.2 (2025-07-24)

- Added a list filter for Checklist protocols to the Django Admin.
- Fixed APILoader so it now saves duration, distance, etc. for all protocols.

## 0.3.1 (2025-07-24)

- Updated APILoader as familyComName and familySciName in the data from eBird, is optional.

## 0.3.0 (2025-07-24)

- Reset the migrations.

To update the database perform the following steps:

1. Make sure you have upgraded to ebird-api-data 0.2.3 and have run the migrations.
2. Run the following command:
   ```python manage.py migrate data zero --fake```
3. Install ebird-api-date 0.3.0:
   ```uv add ebird-api-data==0.3.0```
4. Run the following command:
   ```python manage.py migrate data --fake-initial``` 

## 0.2.3 (2025-07-24)

- Added timestamp fields to track when records are updated.
- Updated APILoader as familyCode, in the data from eBird, is optional.

## 0.2.2 (2025-07-23)

- Added all values to the Species.Category choices.
- Added text choices for Checklist protocols.

## 0.2.1 (2025-07-17)

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
