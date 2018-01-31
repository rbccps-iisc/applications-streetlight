/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9-dev at Wed Jan 31 10:43:05 2018. */

#ifndef PB_ACTUATED_PB_H_INCLUDED
#define PB_ACTUATED_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _ctrlPolicy {
    ctrlPolicy_AUTO_LUX = 0,
    ctrlPolicy_AUTO_TIMER = 1,
    ctrlPolicy_MANUAL = 2
} ctrlPolicy;
#define _ctrlPolicy_MIN ctrlPolicy_AUTO_LUX
#define _ctrlPolicy_MAX ctrlPolicy_MANUAL
#define _ctrlPolicy_ARRAYSIZE ((ctrlPolicy)(ctrlPolicy_MANUAL+1))

/* Struct definitions */
typedef struct __targetAutoLuxParams {
    bool has_targetOnLux;
    uint32_t targetOnLux;
    bool has_targetOffLux;
    uint32_t targetOffLux;
/* @@protoc_insertion_point(struct:_targetAutoLuxParams) */
} _targetAutoLuxParams;

typedef struct __targetAutoTimerParams {
    bool has_targetOnTime;
    uint32_t targetOnTime;
    bool has_targetOffTime;
    uint32_t targetOffTime;
/* @@protoc_insertion_point(struct:_targetAutoTimerParams) */
} _targetAutoTimerParams;

typedef struct __targetControlPolicyParams {
    ctrlPolicy targetControlPolicy;
/* @@protoc_insertion_point(struct:_targetControlPolicyParams) */
} _targetControlPolicyParams;

typedef struct __targetManualControlParams {
    bool has_targetBrightnessLevel;
    uint32_t targetBrightnessLevel;
/* @@protoc_insertion_point(struct:_targetManualControlParams) */
} _targetManualControlParams;

typedef struct __targetPowerStateParams {
    bool targetPowerState;
/* @@protoc_insertion_point(struct:_targetPowerStateParams) */
} _targetPowerStateParams;

typedef struct __targetConfigurations {
    bool has_targetPowerState;
    _targetPowerStateParams targetPowerState;
    bool has_targetControlPolicyParams;
    _targetControlPolicyParams targetControlPolicyParams;
    bool has_targetAutoTimerParams;
    _targetAutoTimerParams targetAutoTimerParams;
    bool has_targetAutoLuxParams;
    _targetAutoLuxParams targetAutoLuxParams;
    bool has_targetManualControlParams;
    _targetManualControlParams targetManualControlParams;
/* @@protoc_insertion_point(struct:_targetConfigurations) */
} _targetConfigurations;

/* Default values for struct fields */

/* Initializer values for message structs */
#define _targetPowerStateParams_init_default     {0}
#define _targetControlPolicyParams_init_default  {(ctrlPolicy)0}
#define _targetManualControlParams_init_default  {false, 0}
#define _targetAutoTimerParams_init_default      {false, 0, false, 0}
#define _targetAutoLuxParams_init_default        {false, 0, false, 0}
#define _targetConfigurations_init_default       {false, _targetPowerStateParams_init_default, false, _targetControlPolicyParams_init_default, false, _targetAutoTimerParams_init_default, false, _targetAutoLuxParams_init_default, false, _targetManualControlParams_init_default}
#define _targetPowerStateParams_init_zero        {0}
#define _targetControlPolicyParams_init_zero     {(ctrlPolicy)0}
#define _targetManualControlParams_init_zero     {false, 0}
#define _targetAutoTimerParams_init_zero         {false, 0, false, 0}
#define _targetAutoLuxParams_init_zero           {false, 0, false, 0}
#define _targetConfigurations_init_zero          {false, _targetPowerStateParams_init_zero, false, _targetControlPolicyParams_init_zero, false, _targetAutoTimerParams_init_zero, false, _targetAutoLuxParams_init_zero, false, _targetManualControlParams_init_zero}

/* Field tags (for use in manual encoding/decoding) */
#define _targetAutoLuxParams_targetOnLux_tag     1
#define _targetAutoLuxParams_targetOffLux_tag    2
#define _targetAutoTimerParams_targetOnTime_tag  1
#define _targetAutoTimerParams_targetOffTime_tag 2
#define _targetControlPolicyParams_targetControlPolicy_tag 1
#define _targetManualControlParams_targetBrightnessLevel_tag 1
#define _targetPowerStateParams_targetPowerState_tag 1
#define _targetConfigurations_targetPowerState_tag 1
#define _targetConfigurations_targetControlPolicyParams_tag 2
#define _targetConfigurations_targetAutoTimerParams_tag 3
#define _targetConfigurations_targetAutoLuxParams_tag 4
#define _targetConfigurations_targetManualControlParams_tag 5

/* Struct field encoding specification for nanopb */
extern const pb_field_t _targetPowerStateParams_fields[2];
extern const pb_field_t _targetControlPolicyParams_fields[2];
extern const pb_field_t _targetManualControlParams_fields[2];
extern const pb_field_t _targetAutoTimerParams_fields[3];
extern const pb_field_t _targetAutoLuxParams_fields[3];
extern const pb_field_t _targetConfigurations_fields[6];

/* Maximum encoded size of messages (where known) */
#define _targetPowerStateParams_size             2
#define _targetControlPolicyParams_size          2
#define _targetManualControlParams_size          6
#define _targetAutoTimerParams_size              12
#define _targetAutoLuxParams_size                12
#define _targetConfigurations_size               44

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define ACTUATED_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
