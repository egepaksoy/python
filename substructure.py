def search(self):
    response = []
    z = 0
    while z < len(self):
        if self[z] == ' ':
            response.append(self[:z])
            self = self[z+1:]
            z = 0
        if z == len(self)-1:
            response.append(self)
            break
        else:
            z += 1
    return response

def molds(self):
    response = []
    z = 0
#                   0               1                       2                               3                                              4                                                                       5
    molds = [['hi', 'hello'],['how are you'] , ["how it's going", "whats up"], ["what are you doing"], ['im fine', 'thanks', 'fine', 'im good', 'i feel good', 'i feel great', 'i feel fine'], ['not a real answer', 'not an answer']]

    for x in molds:
        for y in x:
            for a in search(self):
                if a in search(y):
                    z = 0
                    response.append(y)

    return response, self, molds


def search_algorithm(self):
    self = self.lower()
    self = molds(self)
    key_num = 0
    key_val = ''
    response = self[0]
    control = self[1]
    for a in response:
        if a == control[0] and a[:3] == control[:3]:
            num = response.count(a) + 1
        else:
            num = response.count(a)

        if num > key_num:
            key_num = num
            key_val = a
    return key_val

#! import substructure
#! print(substructure.search_algorithm(''))