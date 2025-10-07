[app]

# (str) Title of your application
title = MyTrackingApp

# (str) Package name (must be lowercase, no spaces)
package.name = mytrackingapp

# (str) Package domain (reverse DNS, must be unique)
package.domain = org.mycompany

# (str) Source code directory (where main.py is)
source.dir = .

# (str) Application entry point (your main file)
source.main = main.py

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,Pillow,plyer,boto3

# (list) Permissions needed
android.permissions = INTERNET,ACCESS_FINE_LOCATION,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (str) Filename for the final APK
package.filename = MyTrackingApp

# (str) Application icon (optional, PNG only)
# icon.filename = %(source.dir)s/icon.png

# (bool) Indicate if the application should be fullscreen
fullscreen = 0


[buildozer]

# (str) Log level (info, debug, error, critical)
log_level = 2

# (bool) Display log messages
verbose = 1

# (str) Android entry point, default is ok
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android application theme, default is ok
# android.theme = @android:style/Theme.NoTitleBar

# (list) Additional Java .jar files to add
# android.add_jars =

# (list) Permissions to remove (comma-separated)
# android.remove_permissions =

# (str) Android min SDK version
android.minapi = 21

# (str) Android target SDK version
android.api = 33

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK version
android.sdk = 33

# (bool) Indicate if logcat should be shown while deploying
logcat = 1
