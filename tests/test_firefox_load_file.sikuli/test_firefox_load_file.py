# if you are putting your test script folders under {git project folder}/tests/, it will work fine.
# otherwise, you either add it to system path before you run or hard coded it in here.
# library_path = "/".join(getParentFolder().split("/")[:-2]) + "/lib/sikuli"
# sys.path.append(library_path)
import browser
import common
import sys


com = common.General()
ff = browser.Firefox()

ff.clickBar()
ff.enterLink("https://docs.google.com/document/d/1EpYUniwtLvBbZ4ECgT_vwGUfTHKnqSWi7vgNJQBemFk/edit")

wait(6)
ff.getConsoleInfo("window.performance.timing")
com.dumpToJson(Env.getClipboard(), "timing" + sys.argv[1])
