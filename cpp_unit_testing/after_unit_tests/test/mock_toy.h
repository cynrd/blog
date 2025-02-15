#ifndef MOCK_TOY__H
#define MOCK_TOY__H

#include <gmock/gmock.h>

#include "toy.h"

class MockToy : public virtual IToy {
public:
  MOCK_METHOD(void, squeak, (), (const, override));
  MOCK_METHOD(void, getChewed, (), (const, override));
};

#endif // MOCK_TOY__H
