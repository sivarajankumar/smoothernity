rm ../../../../build/iphone/Release-iphoneos/Smoothernity.app/Smoothernity
rm -rf ./smoothernity.xcodeproj/xcuserdata/
rm -rf ./smoothernity.xcodeproj/project.xcworkspace/xcuserdata/
xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Release build
