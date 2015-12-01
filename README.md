# Envelope - A Simple Financial Envelope Tool.

(draft - still in progress).

## The problem

I use my credit card to pay most of the things, thus the online banking application is just enough to understand my financial situation.
However, sometimes I need to pay by cash.

1. Tracking cash expenses, without knowing exactly how much you need to spend in advance.
1. Knowing how much cash you have left, without counting.
1. Option for you to edit the last entry, so that you can adjust between your wallet and the envelope.

## Use case

It happens you want to get some cash from the envelope to go to the dentist first, then go out with your friends afterwards.
It's hard to predict how much you'll spend. So you get $400 thinking you shouldn't spend more than that for tonight.
In case of any "emergency" you still have your credit card(s) with you anyway, isn't it? :)

So what you want to do is register that you took $400, and see how much cash is there left, without counting.
Because you are in a rush and your cab is already waiting for you outside.

After a wonderful night out, you check your wallet the next day and find out you only spent $130, because the dentist meeting went pretty well and you don't have any issues. 

You probably don't want to stay with $270 in your wallet, so you decide to add it back to the envelope and edit your last register to reflect that.

**Suggestion:** You want to keep all the receipts in your wallet, until you adjust your last entry. It helps.

# Vagrant environment

I decided to use vagrant here to be able to quickly install a production like environment with gunicorn and nginx as a proof of concept.

## Prerequisites

- VirtualBox 4.3.20 (or later)
- Vagrant 1.7.1 (or later)

## Setup

1. Clone the repository inside the new folder.
2. `cd ./vagrant`
3. `vagrant up`
4. Choose the appropriate network interface to give vagrant internet access. (usually option 1)
6. `vagrant ssh`
7. `sudo /vagrant/bin/install_vagrant.sh`
