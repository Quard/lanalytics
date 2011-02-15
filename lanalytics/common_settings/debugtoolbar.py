
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    # 'debug_toolbar.panels.profiler.ProfilerDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    # 'debug_toolbar.panels.templates.TemplatesDebugPanel',
    # If you are using the profiler panel you don't need the timer
    # 'debug_toolbar.panels.timer.TimerDebugPanel',
)


INTERNAL_IPS = ('127.0.0.1',)