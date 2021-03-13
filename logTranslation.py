import discord

def translateLog(entry : discord.AuditLogEntry, action : discord.AuditLogAction):
    actionList = {
            discord.AuditLogAction.guild_update:        str(entry.target) + ' 항목을 변경했습니다.',
            discord.AuditLogAction.channel_create:      str(entry.target) + ' 채팅 채널을 생성했습니다.',
            discord.AuditLogAction.channel_update:      str(entry.target) + ' 항목을 변경했습니다.',
            discord.AuditLogAction.channel_delete:      str(entry.target) + ' 항목을 제거했습니다.',
            discord.AuditLogAction.overwrite_create:    str(entry.target) + '에 채널 우선 설정 규칙을 생성했습니다.',
            discord.AuditLogAction.overwrite_update:    str(entry.target) + '에 채널 우선 설정 규칙을 업데이트했습니다.',
            discord.AuditLogAction.overwrite_delete:    str(entry.target) + '에 채널 우선 설정 규칙을 제거했습니다.',
            discord.AuditLogAction.kick:                str(entry.target) + '님을 추방했습니다.',
            discord.AuditLogAction.member_prune:        '활동하지 않는 멤버 {0.extra}명을 정리했습니다.'.format(entry),
            discord.AuditLogAction.ban:                 str(entry.target) + '님을 차단했습니다.',
            discord.AuditLogAction.unban:               str(entry.target) + '님의 차단을 해제했습니다.',
            discord.AuditLogAction.member_update:       str(entry.target) + ' 항목을 업데이트했습니다.',
            discord.AuditLogAction.member_role_update:  str(entry.target) + '님의 역할을 업데이트했습니다.',
            discord.AuditLogAction.member_move:         '사용자 {0.extra}명을 {0.extra}로 옮겼습니다.'.format(entry),
            discord.AuditLogAction.member_disconnect:   '사용자 {0.extra}명의 음성 연결을 끊었습니다.'.format(entry),
            discord.AuditLogAction.bot_add:             str(entry.target) + '님을 서버에 추가했습니다.',
            discord.AuditLogAction.role_create:         str(entry.target) + ' 역할을 생성했습니다.',
            discord.AuditLogAction.role_update:         str(entry.target) + ' 역할을 업데이트했습니다.',
            discord.AuditLogAction.role_delete:         str(entry.target) + ' 역할을 삭제했습니다.',
            discord.AuditLogAction.invite_create:       str(entry.target) + ' 초대 코드를 생성했습니다.',
            discord.AuditLogAction.invite_update:       str(entry.target) + ' 초대 코드를 업데이트했습니다.',
            discord.AuditLogAction.invite_delete:       str(entry.target) + ' 초대 코드를 삭제했습니다.',
            discord.AuditLogAction.webhook_create:      str(entry.target) + ' 웹후크를 생성했습니다.',
            discord.AuditLogAction.webhook_update:      str(entry.target) + ' 웹후크를 업데이트했습니다.',
            discord.AuditLogAction.webhook_delete:      str(entry.target) + ' 웹후크를 삭제했습니다.',
            discord.AuditLogAction.emoji_create:        str(entry.target) + ' 이모티콘을 생성했습니다.',
            discord.AuditLogAction.emoji_update:        str(entry.target) + ' 이모티콘을 업데이트했습니다.',
            discord.AuditLogAction.emoji_delete:        str(entry.target) + ' 이모티콘을 삭제했습니다.',
            discord.AuditLogAction.message_delete:      '{0.extra}에서 {0.target}님이 쓴 메세지 {0.extra}개를 삭제했습니다.'.format(entry),
            discord.AuditLogAction.message_bulk_delete: '{0.target}에서 메세지 {0.extra}개를 삭제했습니다.'.format(entry),
            discord.AuditLogAction.message_pin:         '{0.extra}에서 {0.target}님이 쓴 메세지를 고정했습니다.'.format(entry),
            discord.AuditLogAction.message_unpin:       '{0.extra}에서 {0.target}님이 쓴 메세지를 고정 해제했습니다.'.format(entry),
            discord.AuditLogAction.integration_create:  str(entry.target) + ' 연동을 생성했습니다.',
            discord.AuditLogAction.integration_update:  str(entry.target) + ' 연동을 업데이트했습니다.',
            discord.AuditLogAction.integration_delete:  str(entry.target) + ' 연동을 삭제했습니다.'
        }

    return actionList[action]