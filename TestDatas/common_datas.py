'''
'noReset':是否重置app状态，默认false，不需要每次重新安装app，选择true
'unlockType':屏幕锁屏方式，['pin', 'password', 'pattern', 'fingerprint']
'unlockKey':锁屏的key
'automationName':UiAutomator2/Appium(默认)
'''
# desired_caps = {
#                 'platformName':"Android",
#                 'platformVersion':"9.0",
#                 'deviceName':"Android Emulator",
#                 'appActivity':".WebViewBrowserActivity",
#                 'appPackage':"org.chromium.webview_shell",
#                 'noReset':"true" ,
#                 'automationName':"UiAutomator2",
#                 'unlockType':'password',
#                 'unlockKey':'1234'     
#                 }