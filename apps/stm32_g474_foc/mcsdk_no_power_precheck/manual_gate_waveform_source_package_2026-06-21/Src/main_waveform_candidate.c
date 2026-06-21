#include "gate_waveform_candidate.h"

int main(void)
{
  const gate_waveform_candidate_state_t state = gate_waveform_candidate_run_once();
  (void)state;

  for (;;)
  {
    gate_waveform_candidate_force_idle_low();
  }
}
