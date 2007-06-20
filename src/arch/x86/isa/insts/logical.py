# Copyright (c) 2007 The Hewlett-Packard Development Company
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms,
# with or without modification, are permitted provided that the
# following conditions are met:
#
# The software must be used only for Non-Commercial Use which means any
# use which is NOT directed to receiving any direct monetary
# compensation for, or commercial advantage from such use.  Illustrative
# examples of non-commercial use are academic research, personal study,
# teaching, education and corporate research & development.
# Illustrative examples of commercial use are distributing products for
# commercial advantage and providing services using the software for
# commercial advantage.
#
# If you wish to use this software or functionality therein that may be
# covered by patents for commercial use, please contact:
#     Director of Intellectual Property Licensing
#     Office of Strategy and Technology
#     Hewlett-Packard Company
#     1501 Page Mill Road
#     Palo Alto, California  94304
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.  Redistributions
# in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.  Neither the name of
# the COPYRIGHT HOLDER(s), HEWLETT-PACKARD COMPANY, nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.  No right of
# sublicense is granted herewith.  Derivatives of the software and
# output created using the software may be prepared, but only for
# Non-Commercial Uses.  Derivatives of the software may be shared with
# others provided: (i) the others agree to abide by the list of
# conditions herein which includes the Non-Commercial Use restrictions;
# and (ii) such Derivatives of the software include the above copyright
# notice to acknowledge the contribution from this software where
# applicable, this list of conditions and the disclaimer below.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Gabe Black

microcode = '''
def macroop XOR_R_R
{
    xor "env.reg", "env.reg", "env.regm"
};

def macroop XOR_R_I
{
    limm "NUM_INTREGS+1", "IMMEDIATE"
    xor "env.reg", "env.reg", "NUM_INTREGS+1"
};

def macroop XOR_M_R
{
    ld "NUM_INTREGS+1", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
    xor "NUM_INTREGS+1", "NUM_INTREGS+1", "env.reg"
    st "NUM_INTREGS+1", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
};

def macroop XOR_P_R
{
    rdip "NUM_INTREGS+7"
    ld "NUM_INTREGS+1", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
    xor "NUM_INTREGS+1", "NUM_INTREGS+1", "env.reg"
    st "NUM_INTREGS+1", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
};

def macroop XOR_R_M
{
    ld "NUM_INTREGS+1", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
    xor "env.reg", "env.reg", "NUM_INTREGS+1"
};

def macroop XOR_R_P
{
    rdip "NUM_INTREGS+7"
    ld "NUM_INTREGS+1", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
    xor "env.reg", "env.reg", "NUM_INTREGS+1"
};

def macroop AND_R_I
{
    limm "NUM_INTREGS+1", "IMMEDIATE"
    and "env.reg", "env.reg", "NUM_INTREGS+1"
};

def macroop AND_M_I
{
    ld "NUM_INTREGS+2", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
    limm "NUM_INTREGS+1", "IMMEDIATE"
    and "NUM_INTREGS+2", "NUM_INTREGS+2", "NUM_INTREGS+1"
    st "NUM_INTREGS+2", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
};

def macroop AND_P_I
{
    rdip "NUM_INTREGS+7"
    ld "NUM_INTREGS+2", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
    limm "NUM_INTREGS+1", "IMMEDIATE"
    and "NUM_INTREGS+2", "NUM_INTREGS+2", "NUM_INTREGS+1"
    st "NUM_INTREGS+2", 3, ["env.scale", "env.index", "env.base"], \
        "DISPLACEMENT"
};
'''
#let {{
#microcodeString = '''
#    def macroop OR
#    {
#	Or reg reg regm
#    };
#    def macroop NOT
#    {
#	Xor reg reg "0xFFFFFFFFFFFFFFFFULL"
#    };
#'''
#}};
