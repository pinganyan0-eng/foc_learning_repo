#include "gate_test_lockout.h"

int main(void)
{
  gate_test_lockout_init();

  for (;;)
  {
    (void)gate_test_lockout_poll();
  }
}
