#!/bin/sh
#
# Copyright 2012 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

libtoolize && aclocal && autoconf && automake --add-missing
