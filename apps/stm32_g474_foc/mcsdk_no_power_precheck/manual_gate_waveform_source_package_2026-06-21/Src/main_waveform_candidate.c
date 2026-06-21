#include "gate_waveform_candidate.h"

int main(void)
{
  for (;;)
  {
    const gate_waveform_candidate_state_t state = gate_waveform_candidate_run_once();
    if (!state.window_completed || !state.nfault_high)
    {
      for (;;)
      {
        gate_waveform_candidate_force_idle_low();
      }
    }
  }
}
