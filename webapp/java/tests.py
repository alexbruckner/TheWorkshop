"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        # http://py4j.sourceforge.net/
        # make sure that com.bru.workshop.Application is running
        from py4j.java_gateway import JavaGateway
        gateway = JavaGateway()                   # connect to the JVM
        random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
        number1 = random.nextInt(10)              # call the Random.nextInt method
        number2 = random.nextInt(10)
        addition_app = gateway.entry_point        # get the AdditionApplication instance
        number3 = addition_app.addition(number1,number2)
        print "%s + %s = %s" % (number1,number2,number3)
        self.assertEqual(number1 + number2, number3)

    def test_on_the_fly_compilation(self):
        # http://py4j.sourceforge.net/
        # make sure that com.bru.workshop.Application is running
        from py4j.java_gateway import JavaGateway
        app = JavaGateway().entry_point
        value = app.compileAndExecute('Test',''' public class Test {
                                            public static Object execute(){
                                                return "success";
                                            }
                                        }''')
        print value
        self.assertEqual(value, 'success')