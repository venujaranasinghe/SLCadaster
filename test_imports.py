#!/usr/bin/env python3
"""
Test script to verify SL Cadaster plugin imports work correctly
"""

def test_plugin_imports():
    try:
        print("Testing plugin imports...")
        
        # Test basic PyQt5 imports
        from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
        from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox
        from PyQt5.QtGui import QIcon
        print("✓ PyQt5 imports successful")
        
        # Test resources import
        import resources
        print("✓ Resources import successful")
        
        # Test dialog import
        from SL_Cadaster_dialog import SLCadasterDialog
        print("✓ Dialog import successful")
        
        # Test QGIS imports
        from qgis.core import QgsProject, QgsVectorLayer, QgsExpression, QgsFeatureRequest
        print("✓ QGIS core imports successful")
        
        # Test main plugin import
        from SL_Cadaster import SLCadaster
        print("✓ Main plugin import successful")
        
        print("\n🎉 All imports successful! Plugin should load properly in QGIS.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    test_plugin_imports()