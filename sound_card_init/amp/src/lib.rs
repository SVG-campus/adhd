// Copyright 2021 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//! `amp` crate provides `Amp` trait for amplifier initializations and `AmpBuilder`
//! to create `Amp` objects.
#![deny(missing_docs)]

mod alc1011;
mod max98373d;
mod max98390d;
use std::path::PathBuf;

use alc1011::ALC1011;
use dsm::Error;
use max98373d::Max98373;
use max98390d::Max98390;

type Result<T> = std::result::Result<T, Error>;
const CONF_DIR: &str = "/etc/sound_card_init";

/// It creates `Amp` object based on the speaker amplifier name.
pub struct AmpBuilder<'a> {
    sound_card_id: &'a str,
    amp: &'a str,
    config_path: PathBuf,
}

impl<'a> AmpBuilder<'a> {
    /// Creates an `AmpBuilder`.
    /// # Arguments
    ///
    /// * `card_name` - card name.
    /// * `amp` - speaker amplifier name.
    /// * `conf_file` - config file name.
    pub fn new(sound_card_id: &'a str, amp: &'a str, conf_file: &'a str) -> Self {
        let config_path = PathBuf::from(CONF_DIR).join(conf_file);
        AmpBuilder {
            sound_card_id,
            amp,
            config_path,
        }
    }

    /// Creates an `Amp` based on the speaker amplifier name.
    pub fn build(&self) -> Result<Box<dyn Amp>> {
        match self.amp {
            "MAX98390" => {
                Ok(Box::new(Max98390::new(self.sound_card_id, &self.config_path)?) as Box<dyn Amp>)
            }
            "MAX98373" => {
                Ok(Box::new(Max98373::new(self.sound_card_id, &self.config_path)?) as Box<dyn Amp>)
            }
            "ALC1011" => {
                Ok(Box::new(ALC1011::new(self.sound_card_id, &self.config_path)?) as Box<dyn Amp>)
            }
            _ => Err(Error::UnsupportedAmp(self.amp.to_owned())),
        }
    }
}

/// It defines the required functions of amplifier objects.
pub trait Amp {
    /// The amplifier boot time calibration flow.
    fn boot_time_calibration(&mut self) -> Result<()>;
}
