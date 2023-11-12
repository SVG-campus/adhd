/* Copyright 2021 The ChromiumOS Authors
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE file.
 */

#ifndef CRAS_SRC_COMMON_CRAS_STRING_H_
#define CRAS_SRC_COMMON_CRAS_STRING_H_

#include <stdbool.h>
#include <string.h>

#include "third_party/strlcpy/strlcpy.h"

#ifdef __cplusplus
extern "C" {
#endif

// Therad safe version of strerror(3)
const char* cras_strerror(int errnum);

static inline bool str_has_prefix(const char* str, const char* prefix) {
  return 0 == strncmp(str, prefix, strlen(prefix));
}

// Use this with presumption that str1 and/or str2 is null-terminated.
// e.g. compare to string literal: str_equals(s, "foo")
static inline bool str_equals(const char* str1, const char* str2) {
  if (!str1 || !str2) {
    return false;
  }

  return !strcmp(str1, str2);
}

// Use this when neither str1 nor str2 is guaranteed to be null-terminated.
// Note this differs from strncmp which is compared within a range. Instead,
// this returns false if either str1 or str2 is not null-terminated within max
// characters.
static inline bool str_equals_bounded(const char* str1,
                                      const char* str2,
                                      size_t max) {
  if (!str1 || !str2) {
    return false;
  }

  return !strncmp(str1, str2, max) && memchr(str1, 0, max) &&
         memchr(str2, 0, max);
}

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // CRAS_SRC_COMMON_CRAS_STRING_H_
