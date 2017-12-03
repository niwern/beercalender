import random


class Calender(object):
    lines = ""
    width = 4
    height = 6

    def set_numbers(self):
        self.lines = ""
        numbers = []
        for i in range(self.width * self.height):
            numbers.append(i+1)

        for y in range(self.height):
            line = ""
            for x in range(self.width):
                index = random.randint(0, len(numbers)-1)
                line += str((numbers[index])) + ";"
                del numbers[index]
            line = line[:-1]  # cuts the last char ";" of
            self.lines += line + "\n"
        self.lines = self.lines[:-1]
        print(self.lines)

        # convert into string
        """
        for i in range(self.height):
            line = ""
            for j in range(self.width):
                line += str(calender[i][j])
                if j < self.width - 1:
                    line += ';'
            self.lines += line + "\n" """

    def read_from_doc(self):
        f = open('Beer_calender.csv', "r")
        self.lines += f.read()
        print(self.lines)
        if self.lines == "":
            return True
        return False

    def write_to_doc(self):
        f = open('Beer_calender.csv', "w")
        f.write(self.lines)
        f.close()


beer = Calender()
if beer.read_from_doc():
    beer.set_numbers()
    beer.write_to_doc()
