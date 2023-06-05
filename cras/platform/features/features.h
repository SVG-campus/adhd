/*
 * Copyright 2023 The ChromiumOS Authors
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE file.
 */

#ifndef CRAS_PLATFORM_FEATURES_FEATURES_H_
#define CRAS_PLATFORM_FEATURES_FEATURES_H_

#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define DEFINE_FEATURE(name, default_enabled) name,
enum cras_feature_id {
#include "cras/platform/features/features.inc"
#undef DEFINE_FEATURE
  NUM_FEATURES,
};

// Initialize the cras_features backend.
// Returns a negative error code on failure, 0 on success.
int cras_features_init();

// Clean up resources associated with the cras_features backend.
void cras_features_deinit();

// Get whether the feature is enabled.
bool cras_feature_enabled(enum cras_feature_id id);

#ifdef __cplusplus
}
#endif

#endif
