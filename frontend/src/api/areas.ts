import api from '@/services/api'
import type { AreaInformacion } from './types'

export async function obtenerInformacionArea(slug: string): Promise<AreaInformacion> {
  const { data } = await api.get<AreaInformacion>(`/${slug}`)
  return data
}