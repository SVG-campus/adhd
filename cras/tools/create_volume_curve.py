#!/usr/bin/python
#
# Copyright 2012 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

def GenerateSimpleStep(name, max_volume, step_size):
  print '[%s]' % name
  print '  ; Generated by create_volume_curve.py'
  print '  ; simple_step curve, max %d, step %d' % (max_volume, step_size)
  print '  volume_curve = simple_step'
  print '  volume_step = %d' % step_size
  print '  max_volume = %d' % max_volume

def WriteExplicitCurveVal(step, value):
  print '  db_at_%d = %d' % (step, value)

def GenerateExplicit(name):
  print '[%s]' % name
  print '  ; Generated by create_volume_curve.py'
  print '  ; explicit curve'
  print '  volume_curve = explicit'
  for i in range(100):
    print 'Level at step %d:' % (100 - i)
    level = int(raw_input(">"))
    WriteExplicitCurveVal(100 - i, level)
  print 'Level at step 0:'
  level = int(raw_input(">"))
  WriteExplicitCurveVal(0, level)

def GenerateTwoSlope(name, max_volume, step_1, step_2, pivot_point):
  print '[%s]' % name
  print '  ; Generated by create_volume_curve.py'
  print ('  ; two_slope, max = %d, pivot = %d, steps %d, %d' %
         (max_volume, pivot_point, step_1, step_2))
  print '  volume_curve = explicit'
  for i in range(0, (100 - pivot_point)):
    WriteExplicitCurveVal(100 - i, max_volume - step_1 * i)
  pivot_dB_val = max_volume - step_1 * (100 - pivot_point)
  WriteExplicitCurveVal(pivot_point, max_volume - step_1 * (100 - pivot_point))
  for i in range(1, pivot_point):
    WriteExplicitCurveVal(pivot_point - i,  pivot_dB_val - step_2 * i)
  WriteExplicitCurveVal(0, pivot_dB_val - pivot_point * step_2)

def main():
  print 'What is the name of the jack or output to generate a curve for?'
  jack_name = raw_input(">");
  print 'Which type of curve? (simple_step, explicit, two_slope): '
  curve_type = raw_input(">");
  if curve_type == 'simple_step':
    print 'max volume (dBFS * 100):'
    max_volume = int(raw_input(">"))
    print 'step size (in dBFS * 100)'
    step_size = int(raw_input(">"))
    GenerateSimpleStep(jack_name, max_volume, step_size)
  elif curve_type == 'explicit':
    GenerateExplicit(jack_name)
  elif curve_type == 'two_slope':
    print 'max volume (dBFS * 100):'
    max_volume = int(raw_input(">"))
    print 'Volume step where slope changes:'
    pivot_point = int(raw_input(">"))
    print 'step size 100 to %d(in dBFS * 100)' % pivot_point
    step_1 = int(raw_input(">"))
    print 'step size %d to 0(in dBFS * 100)' % pivot_point
    step_2 = int(raw_input(">"))
    GenerateTwoSlope(jack_name, max_volume, step_1, step_2, pivot_point)

if __name__ == '__main__':
  main()
