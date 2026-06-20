#ifndef GATE_TEST_LOCKOUT_H
#define GATE_TEST_LOCKOUT_H

#include <stdbool.h>
#include <stdint.h>

typedef struct
{
  bool nfault_high;
  bool fault_latched;
  bool tim1_outputs_disabled;
  bool tim1_main_output_disabled;
} gate_test_lockout_state_t;

void gate_test_lockout_init(void);
gate_test_lockout_state_t gate_test_lockout_poll(void);
void gate_test_lockout_force_safe_state(void);

#endif
