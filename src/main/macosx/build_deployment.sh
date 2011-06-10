rm build/Deployment/Smoothernity.app/Contents/MacOS/Smoothernity
xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Deployment build
strip -SXx build/Deployment/Smoothernity.app/Contents/MacOS/Smoothernity
