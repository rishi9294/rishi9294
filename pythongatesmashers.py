{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "22b48ca5-7159-48f7-b715-b6d00481ce04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'varun', 'age': 32, 'city': 'gandhinagar'}\n",
      "72.5\n",
      "varun\n",
      "gandhinagar\n",
      "32\n"
     ]
    }
   ],
   "source": [
    "#integers\n",
    "age=32\n",
    "#float\n",
    "weight=72.50\n",
    "#string\n",
    "name=\"varun\"\n",
    "#boolean\n",
    "is_boy=True\n",
    "#list\n",
    "list1=[100,200,300]\n",
    "#dictionary\n",
    "dict1={'name':'varun','age':32,'city':'gandhinagar'}\n",
    "print(dict1)\n",
    "print(weight)\n",
    "print(name)\n",
    "type(list1)\n",
    "print(dict1['city'])\n",
    "print(age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "acdc5477-6557-45ff-8d12-dcf465a867a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(10, 20, 30)\n",
      "None\n",
      "range(1, 5)\n",
      "{1, 2, 3, 4, 5, 6}\n",
      "b'ABa'\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "range"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#tuple\n",
    "tup=(10,20,30)\n",
    "#set\n",
    "set1={1,2,3,4,5,6}\n",
    "#none\n",
    "house_no=None\n",
    "#complex\n",
    "com=1+2j\n",
    "#range\n",
    "num=range(1,5)\n",
    "#bytes and bytearray\n",
    "byte=bytes([65,66,97])\n",
    "\n",
    "print(tup)\n",
    "print(house_no)\n",
    "print(num)\n",
    "print(set1)\n",
    "print(byte)\n",
    "type(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "518251dc-046a-4414-ab38-724c0b8f71e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter first number 10\n",
      "enter second number 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "num1=int(input(\"enter first number\"))\n",
    "num2=int(input(\"enter second number\"))\n",
    "print(num1+num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "871f7dce-cb3c-4077-804f-8f42bd2524bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40.5\n",
      "410.0\n"
     ]
    }
   ],
   "source": [
    "num1=20\n",
    "num2=20.5\n",
    "print(num1+num2)\n",
    "print(num1*num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "5ae2ca09-c6bb-4946-b03b-b0df64737489",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11.0\n",
      "0xb\n",
      "0o13\n",
      "0b1011\n",
      "65\n",
      "A\n"
     ]
    }
   ],
   "source": [
    "a=11\n",
    "f=float(a)\n",
    "print(f)\n",
    "b=hex(a)\n",
    "print(b)\n",
    "c=oct(a)\n",
    "print(c)\n",
    "d=bin(a)\n",
    "print(d)\n",
    "char='A'\n",
    "e= ord(char)\n",
    "print(e)\n",
    "e=65\n",
    "char=chr(e)\n",
    "print(char)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3568094a-e436-461c-abd4-f3b49ceab945",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I'LL CALL YOU LATER\n",
      "I'LL CALL YOU LATER\n"
     ]
    }
   ],
   "source": [
    "#backslash character\n",
    "print('I\\'LL CALL YOU LATER')\n",
    "#OR\n",
    "print(\"I'LL CALL YOU LATER\") #desi jugaad\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ca357e8f-c039-4595-8858-21a0384064bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "prepare well for \"GATE-2026\" exam\n",
      "prepare well for \"GATE-2026\" exam\n"
     ]
    }
   ],
   "source": [
    "print(\"prepare well for \\\"GATE-2026\\\" exam\")\n",
    "#0R\n",
    "print('prepare well for \"GATE-2026\" exam') #desi jugaad\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f80354d6-4614-4835-9f0f-8ea54b583e5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello,RISHI SHARMA!!\n"
     ]
    }
   ],
   "source": [
    "a=\"Hello,RISHI SHARMA!!\"\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0ca75d75-598f-446e-bdcc-f199b26d5183",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello,\n",
      "RISHI SHARMA!!\n"
     ]
    }
   ],
   "source": [
    "a=\"Hello,\\nRISHI SHARMA!!\"\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a429e952-06ad-4687-9d3e-7f0512267a64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello,\t\t\tRISHI SHARMA!!\n"
     ]
    }
   ],
   "source": [
    "#\\t:used to give spaces\n",
    "a=\"Hello,\\t\\t\\tRISHI SHARMA!!\"\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "b71bec6d-aeb0-4efe-a63a-917e804a79fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is b\n"
     ]
    }
   ],
   "source": [
    "a=True\n",
    "b=False\n",
    "\n",
    "if not a: #this will not be executed\n",
    "    print(\"my name is a\")\n",
    "if not b:\n",
    "     print(\"my name is b\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "d49e4287-88db-4745-8bb0-712e2993a719",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your name rishi \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "access denied, you are not registered\n"
     ]
    }
   ],
   "source": [
    "#MEMBERSHIP OPERATORS\n",
    "reg_user=[\"varun\",\"ravi\",\"satish\",\"nitin\"]\n",
    "name=input(\"enter your name\")\n",
    "\n",
    "if name in reg_user:\n",
    "    print(\"access granted,welcome bro\")\n",
    "else:\n",
    "    print(\"access denied, you are not registered\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7d63fae2-2e05-476f-9958-883f73175ca2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "140729826133400\n"
     ]
    }
   ],
   "source": [
    "#identity operator (IS/IS NOT)\n",
    "x=10\n",
    "y=10\n",
    "print(x is y )\n",
    "print(id(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "a82bde22-fcb5-45af-bd11-8662a7577e71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "140729826133400\n",
      "140729826133400\n",
      "140729826133400\n"
     ]
    }
   ],
   "source": [
    "x=10\n",
    "y=10\n",
    "z=x\n",
    "print(z is x)\n",
    "print(x is not y)\n",
    "print(id(x))\n",
    "print(id(y))\n",
    "print(id(z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "3a95265d-58bf-4318-b47f-6363ed23562b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[44]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[32m      4\u001b[39m \u001b[38;5;28mlen\u001b[39m(first_string)\n\u001b[32m      5\u001b[39m first_string[\u001b[32m1\u001b[39m]\n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m \u001b[43mfirst_string\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m1\u001b[39;49m\u001b[43m]\u001b[49m=\u001b[33m'\u001b[39m\u001b[33mo\u001b[39m\u001b[33m'\u001b[39m\n\u001b[32m      7\u001b[39m first_string[\u001b[32m1\u001b[39m:\u001b[32m4\u001b[39m]\n",
      "\u001b[31mTypeError\u001b[39m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "#strings\n",
    "first_string='hello world'\n",
    "print(first_string)\n",
    "len(first_string)\n",
    "first_string[1]\n",
    "first_string[1]='o'\n",
    "first_string[1:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "35dc7176-5d3a-40dc-b25f-fc5eefa8bc8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello, world!\n",
      "13\n",
      "e\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'ell'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "first_string='hello, world!'\n",
    "print(first_string)\n",
    "print(len(first_string))\n",
    "print(first_string[1])\n",
    "first_string[1:4] #slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "7e6335c7-9fbf-4189-96d1-0a40d6bfc3d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "#concatination\n",
    "string1='hello'\n",
    "string2='world'\n",
    "string3= string1+' '+string2\n",
    "print(string3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "47ec63ed-ba77-4072-a1b2-1ae390f291d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "first name is rishi,last name is sharma,& age is 18\n"
     ]
    }
   ],
   "source": [
    "first='rishi'\n",
    "last='sharma'\n",
    "age=18\n",
    "print(f'first name is {first},last name is {last},& age is {age}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "5c8a3dc6-a2a8-4598-a4aa-1cb0c11468be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my first name is rishi,my last name is sharma,& my age is 18\n"
     ]
    }
   ],
   "source": [
    "first='rishi'\n",
    "last='sharma'\n",
    "age=18\n",
    "newone='my first name is {},my last name is {},& my age is {}'. format(first,last,age)\n",
    "print(newone)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
