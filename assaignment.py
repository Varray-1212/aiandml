{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"assaignment","provenance":[{"file_id":"1eBpZpwC602L_a3NnAdT72lXZx1loQFf0","timestamp":1590654350907}],"collapsed_sections":[],"authorship_tag":"ABX9TyOqKPuzvMR8T+eNQOicxj3s"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"ugLT0iTIYugn","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"lLjNd6wBgjrb","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"EcDCBc9x7mty","colab_type":"code","outputId":"ea9a00e2-7e6c-406a-a598-8a0ba2099ac9","executionInfo":{"status":"ok","timestamp":1590653916374,"user_tz":-330,"elapsed":3786,"user":{"displayName":"CHITTMELLA VARUN CHITTMELLA VARUN","photoUrl":"","userId":"09266222750327969323"}},"colab":{"base_uri":"https://localhost:8080/","height":191}},"source":["a=int(input(\"enter the a\"))\n","f1=0\n","f2=1\n","print(f1)\n","print(f2)\n","i=2\n","while i<a:\n","  f3=f1+f2\n","  print(f3)\n","  f1=f2\n","  f2=f3\n","  i=i+1\n","  \n"],"execution_count":0,"outputs":[{"output_type":"stream","text":["enter the a9\n","0\n","1\n","1\n","2\n","3\n","5\n","8\n","13\n","21\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"05fDtHzEfJtr","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"I7CAnyFoQCU4","colab_type":"code","outputId":"906198d7-c32a-4df9-d33e-6ca0fc7dc3fa","executionInfo":{"status":"ok","timestamp":1590603838710,"user_tz":-330,"elapsed":33641,"user":{"displayName":"CHITTMELLA VARUN CHITTMELLA VARUN","photoUrl":"","userId":"09266222750327969323"}},"colab":{"base_uri":"https://localhost:8080/","height":121}},"source":["a=int(input('enter the value'))\n","i=1\n","while i<=a:\n","  j=1\n","  while j<=i:\n","    print(\"*\",end=\"\")\n","    j=j+1\n","  print(\"\\t\")\n","  i=i+1"],"execution_count":0,"outputs":[{"output_type":"stream","text":["enter the value5\n","*\t\n","**\t\n","***\t\n","****\t\n","*****\t\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"hB6kxMQJfYWq","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"oss6ncQPdZ4V","colab_type":"code","outputId":"6a134d9f-eb90-4666-ca12-a195d548ba5f","executionInfo":{"status":"ok","timestamp":1590605921309,"user_tz":-330,"elapsed":32524,"user":{"displayName":"CHITTMELLA VARUN CHITTMELLA VARUN","photoUrl":"","userId":"09266222750327969323"}},"colab":{"base_uri":"https://localhost:8080/","height":104}},"source":["a=int(input(\"a value\"))\n","b=int(input(\"b value\"))\n","c=int(input(\"c value\"))\n","e=((b**2)-(4*a*c))**(1/2)\n","d=(-b+e)/2*a\n","f=(-b-e)/2*a\n","print(d)\n","print(f)"],"execution_count":0,"outputs":[{"output_type":"stream","text":["a value1\n","b value4\n","c value2\n","-0.5857864376269049\n","-3.414213562373095\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"0JE8Fo9bfm7V","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"GiKGOJKAbzSo","colab_type":"code","outputId":"64c46bcd-ac05-4c05-f20f-864de2b649de","executionInfo":{"status":"ok","timestamp":1590605016471,"user_tz":-330,"elapsed":8803,"user":{"displayName":"CHITTMELLA VARUN CHITTMELLA VARUN","photoUrl":"","userId":"09266222750327969323"}},"colab":{"base_uri":"https://localhost:8080/","height":208}},"source":["a=int(input(\"enter number\"))\n","for i in range(1,11):\n","  print(a,\"x\",i,\"=\",a*i)"],"execution_count":0,"outputs":[{"output_type":"stream","text":["enter number7\n","7 x 1 = 7\n","7 x 2 = 14\n","7 x 3 = 21\n","7 x 4 = 28\n","7 x 5 = 35\n","7 x 6 = 42\n","7 x 7 = 49\n","7 x 8 = 56\n","7 x 9 = 63\n","7 x 10 = 70\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"q1RpT1jYf1MO","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":52},"outputId":"cfc06575-2060-40f5-c859-93f179c93f0c","executionInfo":{"status":"ok","timestamp":1590674172385,"user_tz":-330,"elapsed":4897,"user":{"displayName":"CHITTMELLA VARUN CHITTMELLA VARUN","photoUrl":"","userId":"09266222750327969323"}}},"source":["n=int(input(\"enter the n \"))\n","while n>0:\n","  b=n%2\n","  i=str(b)\n","  print(i,end=\"\")\n","  n=n//2"],"execution_count":10,"outputs":[{"output_type":"stream","text":["enter the n 8\n","0001"],"name":"stdout"}]}]}