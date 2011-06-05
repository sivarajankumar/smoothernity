xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Development clean
xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Deployment clean
rm -rf build
