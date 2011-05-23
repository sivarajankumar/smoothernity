xcodebuild -project smoothernity.xcodeproj -target "smoothernity (Upgraded)" -configuration Development clean
xcodebuild -project smoothernity.xcodeproj -target "smoothernity (Upgraded)" -configuration Deployment clean
rm -rf build
