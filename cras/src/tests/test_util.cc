// Copyright 2023 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "cras/src/tests/test_util.h"

#include <assert.h>

const char* test_tmpdir() {
  const char* dir = getenv("TEST_TMPDIR");
  assert(dir != nullptr);
  return dir;
}
