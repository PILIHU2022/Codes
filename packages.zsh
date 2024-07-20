#!/bin/zsh

# 这样应该在装系统时指定
typeset function get_packages() {
    typeset -a packages=(
        "linux-zen"
        "linux-firmware"
        "base"
        "base-devel"

        "man-db"
        "man-pages"
        "man-pages-zh_cn"

        "vim"
        "neovim"

        "p7zip"
        "unrar"
        "zip"
        "lzip"

        "grub"
        "efibootmgr"
        "os-prober"

        "sudo"
        "fzf"
        "zsh"

        "openssh"
        "git"
        "tree"

        "sl"
        "fastfetch"
        

        "alsa-utils"
        "ffmpeg"
    )
    print -l $packages
}

#get_packages

typeset function install() {
    typeset -a packages=(
        "sddm"
        "plasma-desktop"
        "fcitx5-im"
        "noto-fonts-cjk"
        "ttf-jetbrains-mono-nerd"
    )

    # 安装 KDE、SDDM、输入法框架以及必要的字体
    pacman -S --needed $packages

    packages=(
        "sddm-kcm"
        "plasma-wayland-session"
        "fcitx5-lua"
        "fcitx5-input-support"
        "fcutx5-rime"
    )

    # 安装 SDDM 的，KConfig 模块。
    # 安装 Plasma 的 Wayland 会话
    # 安装输入法的可选依赖
    paru -S --needed --asdeps $packages

    packages=(
        "konsole"
        "yakuake"

        "dolphin"
        "ark"
        "kate"
        "filelight"
        "partitionmanager"
        "sweeper"

        "krdc"
        "krfb"
        "ktorrent"

        "microsoft-edge-stable-bin"

        "kmousetool"
        "kcharselect"

        "gwenview"
        "spectacle"
        "kcolorchooser"
        "krita"

        "ksystemlog"
    )

    # 安装基本应用
    paru -S --needed $package
}