import unittest
import lab2Class
import decorator
import MyJson
import random
import json
import lab2
import Singletone


class Lab2Tests(unittest.TestCase):
    def test_lab2Class(self):
        vec = lab2Class.vector([1, 2, 3])
        vec2 = lab2Class.vector([0, 0, 0])
        vec3 = lab2Class.vector([1, 2, 3])
        vec4 = lab2Class.vector([1, 2, 3, 4])
        vec5 = lab2Class.vector([0,0,0])
        self.assertFalse(vec == vec2)
        self.assertFalse(vec == vec4)
        self.assertTrue(vec2 == vec5)
        self.assertEqual((vec + vec3).vec, [2, 4, 6])
        self.assertEqual((vec - vec3).vec, [0, 0, 0])
        self.assertEqual(vec2.len(), 0)
        self.assertEqual(str(vec2), "0,0,0")
        self.assertEqual(vec[2], 3)
        self.assertEqual(lab2Class.vector.scalar(vec, vec3), 14)
        self.assertFalse(vec == vec4)
        self.assertIsNone(vec[10])
        self.assertIsNone(vec + vec4)
        self.assertIsNone( vec - vec4)
        self.assertIsNone(lab2Class.vector.scalar(vec, vec4))
        self.assertEqual((vec*1).vec, vec.vec)
        self.assertEqual(len(vec),len(vec2))

    def test_decor(self):
        self.assertEqual(decorator.decorator(2), 4)
        self.assertEqual(decorator.decorator(2), 4)
        self.assertEqual(decorator.decorator(22), 44)
        self.assertEqual(decorator.decorator(22), 44)

    def test_json(self):
        Dict = {'Lol': 'Jeez', 4: [5, 4, 3, 2]}
        dict2 = {'Wat': 'Hat'}
        dict3 = {0: [1.1, 2.2, 3.3, 4.4]}
        list1 = ["we", "i", "you"]
        dict4 = {'list': list1}
        list2 = [False, True, None]
        dict5 = {'dict': list2}
        for_dict = {'this': 'that'}
        dict6 = {'dict': for_dict}
        self.assertEqual(MyJson.to_json(Dict), json.dumps(Dict))
        self.assertEqual(MyJson.to_json(dict2), json.dumps(dict2))
        self.assertEqual(MyJson.to_json(dict3), json.dumps(dict3))
        self.assertEqual(MyJson.to_json(dict4), json.dumps(dict4))
        self.assertEqual(MyJson.to_json(dict5), json.dumps(dict5))
        self.assertEqual(MyJson.to_json(dict6), json.dumps(dict6))

    def test_merge(self):
        with open('nums.txt', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(50))
        lab2.merge("nums.txt")
        temp = 1000001
        temp_bool = False
        with open('nums.txt', 'r') as f:
            for lines in f:
                if int(lines) <= int(temp):
                    temp = lines
                    continue
                else:
                    temp_bool = True
                    break
        self.assertTrue(temp_bool)

    def test_singletone(self):  
      a = Singletone.MyClass('1')
      b = Singletone.MyClass('1')
      self.assertIs(a,b)  


