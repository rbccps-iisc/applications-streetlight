/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.9-dev at Thu Aug 17 11:20:02 2017. */

#include "actuated.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t config_values_fields[3] = {
    PB_FIELD(  1, BOOL    , REQUIRED, STATIC  , FIRST, config_values, targetPowerState, targetPowerState, 0),
    PB_FIELD(  3, UENUM   , REQUIRED, STATIC  , OTHER, config_values, targetControlPolicy, targetPowerState, 0),
    PB_LAST_FIELD
};

const pb_field_t config_values_targetManualControlParams_fields[2] = {
    PB_FIELD(  2, UINT32  , OPTIONAL, STATIC  , FIRST, config_values_targetManualControlParams, targetBrightnessLevel, targetBrightnessLevel, 0),
    PB_LAST_FIELD
};

const pb_field_t config_values_targetAutoTimerParams_fields[3] = {
    PB_FIELD(  4, UINT64  , OPTIONAL, STATIC  , FIRST, config_values_targetAutoTimerParams, targetOnTime, targetOnTime, 0),
    PB_FIELD(  5, UINT64  , OPTIONAL, STATIC  , OTHER, config_values_targetAutoTimerParams, targetOffTime, targetOnTime, 0),
    PB_LAST_FIELD
};

const pb_field_t config_values_targetAutoLuxParams_fields[3] = {
    PB_FIELD(  6, UINT32  , OPTIONAL, STATIC  , FIRST, config_values_targetAutoLuxParams, targetOnLux, targetOnLux, 0),
    PB_FIELD(  7, UINT32  , OPTIONAL, STATIC  , OTHER, config_values_targetAutoLuxParams, targetOffLux, targetOnLux, 0),
    PB_LAST_FIELD
};



/* @@protoc_insertion_point(eof) */