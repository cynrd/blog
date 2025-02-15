#include <gtest/gtest.h>
#include "dog.h"
#include "mock_toy.h"
TEST(DogToyTest, SqueaksToy) {
    using namespace ::testing;

    MockToy toy;
    // what we expect (it should be written before the actual method call)
    EXPECT_CALL(toy, squeak).Times(Exactly(1));
    // class under test
    Dog buddy("Buddy", toy);
    // method under test
    buddy.play();
}