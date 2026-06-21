#include "gate_waveform_neutral_wrapper.h"

extern void gate_waveform_candidate_force_idle_low(void);

void gate_waveform_neutral_wrapper_hold_idle_forever(void)
{
  gate_waveform_candidate_force_idle_low();

  for (;;)
  {
    gate_waveform_candidate_force_idle_low();
  }
}

int main(void)
{
  gate_waveform_neutral_wrapper_hold_idle_forever();
}
