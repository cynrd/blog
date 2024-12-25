#include <iostream>
#include <string>

class Toy {
private:
    std::string name;

public:
    Toy(const std::string& name) : name(name) {}

    void squeak() const {
        std::cout << "Toy (" << name << "): *Squeak squeak!*" << std::endl;
    }

    void getChewed() const {
        std::cout << "Toy (" << name << "): Why do you always chew on me?!" << std::endl;
    }
};

class Dog {
private:
    std::string name;
    Toy& toy; // Association: Dog "has a" Toy, passed by reference

public:
    Dog(const std::string& name, Toy& toy) : name(name), toy(toy) {}

    void play() const {
        std::cout << name << ": Oh boy, oh boy! A toy!" << std::endl;
        toy.squeak();
        toy.getChewed();
        std::cout << name << ": BEST. DAY. EVER." << std::endl;
    }

    void display() const {
        std::cout << "Dog Name: " << name << std::endl;
        std::cout << name << " loves their toy: " << std::endl;
        toy.squeak();
    }
};

int main() {
    Toy ball("Squeaky Ball");
    Dog buddy("Buddy", ball); // Pass the toy by reference

    buddy.display();
    buddy.play();

    return 0;
}

