xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Debug clean
xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Release clean
rm -rf ../../../../build/iphone
rm -rf ../../../../temp/iphone
rm -rf ./smoothernity.xcodeproj/xcuserdata/
rm -rf ./smoothernity.xcodeproj/project.xcworkspace/xcuserdata/
