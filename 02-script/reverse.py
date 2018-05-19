import commands
import StringIO

def reverse(debugger, command, result, internal_dict):
    buf = StringIO.StringIO()
    buf.write(debugger.GetSelectedTarget())
    targetName = buf.getvalue();
    if targetName != "":
        result = ""
        for i in xrange(len(targetName) -1, -1, -1):
            result += targetName[i]
        result = "FT_" + result 
        print(result)

def ls(debugger, command, result, internal_dict):
    print >>result, (commands.getoutput('/bin/ls %s' % command))

def man(debugger, command, result, internal_dict):
    print >>result, (commands.getoutput('/usr/bin/man %s' % command))

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f reverse.reverse reverse')
    debugger.HandleCommand('command script add -f reverse.ls ls')
    debugger.HandleCommand('command script add -f reverse.man man')
