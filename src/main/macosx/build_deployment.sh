rm ../../../../build/macosx/Deployment/Smoothernity.app/Contents/MacOS/Smoothernity
rm ./smoothernity.xcodeproj/*.pbxuser
rm ./smoothernity.xcodeproj/*.mode1v3
rm -rf ./smoothernity.xcodeproj/xcuserdata/
rm -rf ./smoothernity.xcodeproj/project.xcworkspace/xcuserdata/
xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Deployment build
strip -SXx ../../../../build/macosx/Deployment/Smoothernity.app/Contents/MacOS/Smoothernity
