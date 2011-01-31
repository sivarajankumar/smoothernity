xcodebuild -project smoothernity.xcodeproj -target "smoothernity (Upgraded)" -configuration Deployment build
strip -SXx build/Deployment/Smoothernity.app/Contents/MacOS/Smoothernity
