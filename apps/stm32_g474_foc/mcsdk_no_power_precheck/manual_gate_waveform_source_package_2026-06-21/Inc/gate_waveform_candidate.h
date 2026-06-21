#ifndef GATE_WAVEFORM_CANDIDATE_H
#define GATE_WAVEFORM_CANDIDATE_H

#include <stdbool.h>
#include <stdint.h>

#if !defined(GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK)
#error "Gate E1 source package only: open and record a dated Gate E2 build-only boundary before compiling."
#endif

#define GATE_WAVEFORM_CANDIDATE_TIMER_HZ       170000000u
#define GATE_WAVEFORM_CANDIDATE_TIMER_TICK_HZ 1000000u
#define GATE_WAVEFORM_CANDIDATE_PWM_HZ        0u
#define GATE_WAVEFORM_CANDIDATE_DUTY_PERMILLE 0u
#define GATE_WAVEFORM_CANDIDATE_WINDOW_PERIODS 1u
#define GATE_WAVEFORM_CANDIDATE_PRE_IDLE_PERIODS 1u
#define GATE_WAVEFORM_CANDIDATE_POST_IDLE_PERIODS 1u
#define GATE_WAVEFORM_CANDIDATE_DEADTIME_DTG  0x90u
#define GATE_WAVEFORM_CANDIDATE_DIAG_STEP_LOOPS       1000000u
#define GATE_WAVEFORM_CANDIDATE_DIAG_INTERSTEP_LOOPS  120000u
#define GATE_WAVEFORM_CANDIDATE_DIAG_IDLE_LOOPS       800000u
#define GATE_WAVEFORM_CANDIDATE_WAKE_LOOPS            6000000u
#define GATE_WAVEFORM_CANDIDATE_DIAG_VECTOR_COUNT     6u

typedef struct
{
  uint32_t timer_hz;
  uint32_t timer_tick_hz;
  uint32_t pwm_hz;
  uint32_t duty_permille;
  uint32_t window_periods;
  uint32_t pre_idle_periods;
  uint32_t post_idle_periods;
  uint32_t deadtime_dtg;
  uint32_t diagnostic_vector_count;
  bool command_ingress_present;
} gate_waveform_candidate_config_t;

typedef struct
{
  bool nfault_high;
  bool fault_latched;
  bool window_completed;
  bool tim1_outputs_disabled;
  bool tim1_main_output_disabled;
} gate_waveform_candidate_state_t;

gate_waveform_candidate_config_t gate_waveform_candidate_get_config(void);
void gate_waveform_candidate_force_idle_low(void);
gate_waveform_candidate_state_t gate_waveform_candidate_run_once(void);

#endif
