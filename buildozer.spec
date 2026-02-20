[app]
title = Tampilan Awalan
package.name = tampilanawalan
package.domain = org.riza

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1.0
requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
