#!/usr/bin/env python3
import librun, libconfig, libstmerge
import time
global helber
helber="""
   --- README of exp14-stringtie2ballgown ---
  Title:
    Batch Processing for StringTie

  Usage:
    python exp14-s2b -t <TRIBE> --control=<Control Group> -g <GROUP,GROUP,GROUP...>

  Data Structure:
    First : tribe,
        e.g. raw, untrim, trimmed...
    Second: group,
        e.g. control, A, B, 1, 2...
    Third : subgroup/files,
        e.g. foward, reverse, pair, unpair

    Visualise graph: explanation01-dataStructure.svg

  Original command:
    stringtie [GROUP BAM file] -B \
    -G [Merged GTF file] -p [thread] -b [Result PATH]

  CAUTION:
    Exp14 required Exp13
    <GROUP> must separate with space
    <GROUP> don't allowed spacing

   --- README ---
""""""
 Postfix of variables:
  -si: String
   -ni: alternative/second string for same Usage
   -fi: string for open()
  -ho: String(that store dir path)
  -ti: Intiger/Float
  -li: List
  -tu: Tuple
  -di: Dictionary
  -fa: File (with open())
  -so: JSON
"""

Marge = libstmerge.loggo()
Confi = libconfig.confi()
class loggo(librun.loggi):
    def pesonai(self):
        # self.testing = True
        self.typesi = 'script'

        self.dicodi = {
            "tribe"   : [],
            "group"   : [],
            "control" : ""
        }
        self.sync()

        self.tagesi = ""

        self.comali = []
        self.adcoli = [ Confi.get("bin/stringtie") ]
        self.adrfli = [ "-G" ]
        self.adphli = [ "-p", Confi.get("run/thread")]
        self.adfoli = [ "-b" ]
        self.adotli = [ "-o" ]


        self.filasi = "exp14-stringtie2ballgown"
        self.libadi = {}
        self.prelogi = Confi.get("result/log")+"/exp14-s2b-"

    def actor(self):
        tibeli = self.dicodi.get("tribe",[])
        gupoli = self.dicodi.get("group",[])
        cotosi = self.dicodi.get("control","")

        self.hedda()

        self.tagesi = Confi.get("result/stringtie")
        self.chkpaf()

        for tibe in tibeli:
            self.printbr()
            Marge.testing = self.testing
            Marge.prelogi = Confi.get("result/log")+"/exp14-s2b-Merge-"

            metali = []
            metali.extend(gupoli)
            metali.append(cotosi)
            Marge.dicodi = {
                "tribe"   : [tibe],
                "group"   : metali
            }
            Marge.actor()
            self.printbr()

            self.adinsi = Marge.outusi
            self.tagesi = self.adinsi
            self.chkfal()

            for gupo in gupoli:

                if cotosi != "":
                    self.comali = []
                    self.comali.extend(self.adcoli)

                    adsbsi = (
                        Confi.get("result/hisat") + "/" +
                        Confi.get("data/prefix/"+tibe) + "-" +
                        gupo + "-stringtie-sorted.bam"
                    )
                    self.comali.append(adsbsi)

                    self.comali.extend(self.adrfli)
                    self.comali.append(self.adinsi)

                    self.comali.extend(self.adphli)

                    self.comali.extend(self.adfoli)
                    adresi = (
                        Confi.get("result/stringtie") + "/" +
                        Confi.get("data/prefix/"+tibe) + "-" +
                        "-".join(sorted([cotosi,gupo]))
                    )
                    self.comali.append(adresi)

                    self.comali.extend(self.adotli)
                    adresi = (
                        Confi.get("result/stringtie") + "/" +
                        Confi.get("data/prefix/"+tibe) + "-" +
                        gupo + "-s2b.gtf"
                    )
                    self.comali.append(adresi)

                    self.ranni()

        self.calti()

Runni = loggo()
