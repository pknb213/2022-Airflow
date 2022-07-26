# import
import subprocess

# class
# res = subprocess.run(["ls", "-l", "./"], capture_output=True)
# print(res.stdout.decode("utf-8"))

# mongo --port 20000 -eval "db.serverStatus({'repl':1})" --quiet | sed 's/\(NumberLong([[:punct:]]\?\)\([[:digit:]]*\)\([[:punct:]]\?)\)/\2/' | sed 's/\(ISODate(\)\(.*\)\()\)/\2/'  | sed 's/Timestamp(\([0-9]*\),[[:space:]]*[[:digit:]]*)/\1/' | sed 's/BinData([[:digit:]],\([^,]*\))/\1/' | sed 's/ObjectId(\([^.]*\))/\1/'
# mongo --port 20000 --eval "db.session.stats(1024)"  --quiet | sed 's/\(NumberLong([[:punct:]]\?\)\([[:digit:]]*\)\([[:punct:]]\?)\)/\2/' | sed 's/\(ISODate(\)\(.*\)\()\)/\2/' | sed 's/Timestamp(\([0-9]*\),[[:space:]]*[[:digit:]]*)/\1/' | sed 's/BinData([[:digit:]],\([^,]*\))/\1/'
# mongo --port 20000 --eval "db.stats(1024)" --quiet | sed 's/\(NumberLong([[:punct:]]\?\)\([[:digit:]]*\)\([[:punct:]]\?)\)/\2/' | sed 's/\(ISODate(\)\(.*\)\()\)/\2/' | sed 's/Timestamp(\([0-9]*\),[[:space:]]*[[:digit:]]*)/\1/' | sed 's/BinData([[:digit:]],\([^,]*\))/\1/'
# mongotop 10 -uri=mongodb://127.0.0.1:27617/userhabit -u admin -p admin --authenticationDatabase=admin --json -n 1
# mongostat 10 -uri=mongodb://127.0.0.1:27617/userhabit -u admin -p admin --authenticationDatabase=admin --json -n 1
# top -bc | head -5 | sed '/top/d'

# Todo: Mongo Cluster에 적재하는 것한 후에 Polaris Dummy Data 넣기, sed 명령어 대신 Python String 변환 하기

with subprocess.Popen(["mongo", "--port", "20000", "--eval", "db.stats(1024)", "--quiet"], stdout=subprocess.PIPE) as cp:
    sed_1 = subprocess.Popen(["sed", "s/\(NumberLong([[:punct:]]\?\)\([[:digit:]]*\)\([[:punct:]]\?)\)/\2/"], stdin=cp.stdout, stdout=subprocess.PIPE)
    cp.wait()
    sed_2 = subprocess.Popen(["sed", "s/\(ISODate(\)\(.*\)\()\)/\2/"], stdin=sed_1.stdout, stdout=subprocess.PIPE)
    sed_1.wait()
    sed_3 = subprocess.Popen(["sed", "s/Timestamp(\([0-9]*\),[[:space:]]*[[:digit:]]*)/\1/"], stdin=sed_2.stdout, stdout=subprocess.PIPE)
    sed_2.wait()
    sed_4 = subprocess.Popen(["sed", "s/BinData([[:digit:]],\([^,]*\))/\1/"], stdin=sed_3.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
    res = sed_4.communicate()[0]
    sed_4.wait()
    print(res)

    with open('db_stats', 'w') as f:
        f.write(res)

with open('test.txt', 'w') as f:
    mongo = subprocess.Popen(["mongo", "--port", "20000", "--eval", "db.serverStatus({'repl':1})"], stdout=subprocess.PIPE)
    head = subprocess.Popen(["head", "-n", "5"], stdin=mongo.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
    mongo.stdout.close()
    output = head.communicate()
    print(output[0])
    # f.write(output[0])



# def
