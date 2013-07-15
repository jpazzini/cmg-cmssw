import FWCore.ParameterSet.Config as cms

#
# $Id: preshowerClusteringSequence.cff,v 1.4 2008/03/03 19:50:58 futyand Exp $
#
#------------------
#Preshower clustering:
#------------------
# producer for endcap SuperClusters including preshower energy
from RecoEcal.EgammaClusterProducers.correctedEndcapSuperClustersWithPreshower_cfi import *
# producer for preshower cluster shapes
from RecoEcal.EgammaClusterProducers.preshowerClusterShape_cfi import *
# create sequence for preshower clustering
preshowerClusteringSequence = cms.Sequence(correctedEndcapSuperClustersWithPreshower*preshowerClusterShape)

