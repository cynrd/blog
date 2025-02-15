#ifndef TOY__H
#define TOY__H
#include <string>

class IToy {
public:
  virtual ~IToy() = default;
  virtual void squeak() const = 0;
  virtual void getChewed() const = 0;
};

class Toy : public virtual IToy {
private:
  std::string name;

public:
  Toy(const std::string &name);
  void squeak() const override;
  void getChewed() const override;
};

#endif // TOY__H
