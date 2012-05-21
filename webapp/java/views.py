# Create your views here.
from py4j.java_gateway import JavaGateway

def test_basic_addition():
    # http://py4j.sourceforge.net/
    # make sure that com.bru.workshop.Application is running
    gateway = JavaGateway()                   # connect to the JVM
    random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
    number1 = random.nextInt(10)              # call the Random.nextInt method
    number2 = random.nextInt(10)
    addition_app = gateway.entry_point        # get the AdditionApplication instance
    number3 = addition_app.addition(number1,number2)
    return  "%s + %s = %s" % (number1,number2,number3)

def java_compile_and_execute(source):
    # http://py4j.sourceforge.net/
    # make sure that com.bru.workshop.Application is running
    return JavaGateway().entry_point.compileAndExecute('Test', source)
