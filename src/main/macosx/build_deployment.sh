rm ../../../../build/macosx/Deployment/Smoothernity.app/Contents/MacOS/Smoothernity
xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Deployment build
strip -SXx ../../../../build/macosx/Deployment/Smoothernity.app/Contents/MacOS/Smoothernity
