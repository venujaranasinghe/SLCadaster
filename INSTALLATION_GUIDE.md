# SL Cadaster Plugin Installation Guide for QGIS 3.x

## Fixed Issues:
✅ **ModuleNotFoundError: No module named 'resources'** - RESOLVED
- Regenerated `resources.py` file for PyQt5 compatibility
- Used QGIS's built-in pyrcc5 compiler

## Installation Steps:

### 1. Copy Plugin Files
Copy the entire SLCadaster folder to your QGIS 3 plugins directory:

**Mac QGIS 3.x:**
```bash
~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/SLCadaster/
```

**Windows QGIS 3.x:**
```bash
%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\SLCadaster\
```

### 2. Restart QGIS
Close and restart QGIS completely.

### 3. Enable Plugin
1. Go to **Plugins** → **Manage and Install Plugins**
2. Click on **Installed** tab
3. Find **SL Cadaster** in the list
4. Check the checkbox to enable it

### 4. Verify Installation
- You should see "SL Cadaster V0.2" in the toolbar or plugins menu
- No error messages should appear in the QGIS log

## Files Updated for QGIS 3.x Compatibility:

1. **metadata.txt** - Updated version requirements
2. **SL_Cadaster.py** - PyQt4→PyQt5 migration, QGIS API updates
3. **SL_Cadaster_dialog.py** - PyQt4→PyQt5 migration
4. **resources.py** - Regenerated for PyQt5
5. **MIGRATION_NOTES.md** - Detailed migration documentation

## Troubleshooting:

### If you get "No module named 'resources'" error:
This should now be fixed. If it persists:
1. Ensure you're using the updated `resources.py` file
2. Check that all files are in the correct plugin directory
3. Restart QGIS completely

### If you get processing algorithm errors:
Some processing algorithms may need parameter updates. The plugin will load but some functions may not work until processing calls are updated for QGIS 3.x.

## Testing the Plugin:
You can run the test script to verify imports:
```bash
cd /path/to/SLCadaster
/Applications/QGIS-LTR.app/Contents/MacOS/bin/python3 test_imports.py
```

## Support:
For issues specific to the migration, check the MIGRATION_NOTES.md file for detailed technical information.