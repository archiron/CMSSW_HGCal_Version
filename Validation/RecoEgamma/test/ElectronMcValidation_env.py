#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys

class env:
    def dd_tier(self):
        dd_tier = 'GEN-SIM-RECO'
        return dd_tier 

    def tag_startup(self):
        tag_startup = '93X_upgrade2023_realistic_v0_D17PU200'
        return tag_startup

    def data_version(self):
        data_version = 'v1'
        return data_version

    def test_global_tag(self):
        test_global_tag = self.tag_startup()
        return test_global_tag

    def dd_cond(self):
        dd_cond = 'PU25ns_' + self.test_global_tag() + '-' + self.data_version()
        return dd_cond


